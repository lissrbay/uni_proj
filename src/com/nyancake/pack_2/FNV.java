package com.nyancake.pack_2;

public class FNV {
	private static final int FNV_INIT = 0x811c9dc5;
    private static final int FNV_PRIME = 0x01000193;
 
	public FNV() {}
    public static int hash32(int sum, final String string) {
    	if (sum == 0)
    		sum = FNV_INIT;
        int result = sum;
        final int len = string.length();
        for(int i = 0; i < len; i++) {
        	result *= FNV_PRIME;
            result ^= (int) string.charAt(i);
        }
        return result;
    }
}
