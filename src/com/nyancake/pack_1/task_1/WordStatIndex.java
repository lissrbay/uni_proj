package com.nyancake.pack_1.task_1;
import java.io.*;
import java.util.LinkedHashMap;
import java.util.Map;

public class WordStatIndex {
	private static Map<String, Integer> dict = new LinkedHashMap<String, Integer>();
	private static final String CHAR_BLACKLIST = "[^A-Za-zÀ-ßà-ÿ'’-]";
	
	public static void main(String[] args) {
		String filePathIn = args[0];
		String filePathOut = args[1];
		input(filePathIn);
		output(filePathOut);
	}
	
	private static void input(String path) {
		BufferedReader reader = null;
		try	{		
			reader = new BufferedReader(new InputStreamReader(
				 		new FileInputStream(path), "UTF-8"));
		} catch (FileNotFoundException ex) {
			System.out.println("File not found.");
		}catch (UnsupportedEncodingException ex)
		{ 
			System.out.println("Use UTF-8 plz."); 
		}

		try	{	
			String currentString = reader.readLine();
			while (currentString != null) {
				parsingString(currentString);
				currentString = reader.readLine();
			}
			reader.close();
		} catch (IOException ex) {
			System.out.println("I/O error.");
		}
	}
	
	private static void parsingString(String currentString) {
		String[] listOfWords = currentString.split(" ");
		for(String word: listOfWords) {
	        word = (word.replaceAll(CHAR_BLACKLIST, "")).toLowerCase();
			if (word.length() > 0)
				dict.put(word, dict.getOrDefault(word, 0) + 1);
		}
	}
	
	private static void output(String path) {
		BufferedWriter writer = null;
		try
		{	writer = new BufferedWriter( new OutputStreamWriter(
			 		new FileOutputStream(path), "UTF-8"));
		} catch (FileNotFoundException ex)
		{
			System.out.println("File not found.");
		}
		 catch (UnsupportedEncodingException ex)
		{  
			 System.out.println("Use UTF-8 plz."); 
		}
		try	{
			for (Map.Entry<String, Integer> elem : dict.entrySet()) 
				writer.append(elem.getKey() + " " + elem.getValue() + "\r\n");
			writer.close();
		} catch (IOException ex) {
			System.out.println("I/O error.");
		}
	}
}
