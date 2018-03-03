package com.nyancake.pack_1.markup;

public class Text extends Paragraph {
	private String info;

   Text(String information){
        info = information;
    }

    public void toMarkdown(StringBuilder resultingString) {
    	resultingString.append(info);
    }
}