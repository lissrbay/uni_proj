package com.nyancake.pack_2;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Walk {
    private List<Integer> hashSum = new ArrayList<Integer>();
    private List<String> files = new ArrayList<String>();
	private final static String CODING = "UTF-8";
	public static void main(String[] args) {
		String filePathIn = args[0];
		String filePathOut = args[1];
		Walk file = new Walk(); 
		file.input(filePathIn);
		file.output(filePathOut);
	}
	
	private void input(String path) {
		BufferedReader reader = null;
		try	{		
			reader = new BufferedReader(new InputStreamReader(new FileInputStream(path), CODING));
		} catch (FileNotFoundException ex) {
			System.out.println("File not found.");
		}catch (UnsupportedEncodingException ex)
		{ 
			System.out.println("Use UTF-8 plz."); 
		}
		try	{	
			String currentString = reader.readLine();
			while (currentString != null) {
				int hash = processingTxt(currentString);
				hashSum.add(hash);
				files.add(currentString);
				currentString = reader.readLine();
			}
			reader.close();
		} catch (IOException ex) {
			System.out.println("I/O error.");
		}
	}
	
	private int processingTxt(String path) {
		int currentSum = 0x00000000;
		BufferedReader reader = null;
		try	{		
			reader = new BufferedReader(new InputStreamReader(new FileInputStream(path), CODING));
		} catch (FileNotFoundException ex) {
			System.out.println(path + " - File not found.");
			return currentSum;
		} catch (UnsupportedEncodingException ex) { 
			System.out.println(path + " - Use UTF-8 plz."); 
			return currentSum;
		}

		try	{	
			String currentString = reader.readLine();
			while (currentString != null) {
				currentSum = FNV.hash32(currentSum, currentString);
				
				currentString = reader.readLine();
			}
			reader.close();
		} catch (IOException ex) {
			System.out.println(path + " - I/O error.");
		}
		return currentSum;
	}
	
	private void output(String path) {
		BufferedWriter writer = null;
		try
		{	writer = new BufferedWriter( new OutputStreamWriter(new FileOutputStream(path), CODING));
		} catch (FileNotFoundException ex)
		{
			System.out.println("File not found.");
		}
		 catch (UnsupportedEncodingException ex)
		{  
			 System.out.println("Use UTF-8 plz."); 
		}
		try	{
			for (int i = 0; i < hashSum.size(); i++) {
				String hex = String.format("%8s", Integer.toHexString(hashSum.get(i)));
				hex = hex.replace(' ','0');
				writer.append(hex + " " + files.get(i) + "\r\n");
			}
			writer.close();
		} catch (IOException ex) {
			System.out.println("I/O error.");
		}
	}
}
