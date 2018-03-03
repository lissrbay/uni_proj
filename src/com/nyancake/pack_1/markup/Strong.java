package com.nyancake.pack_1.markup;

import java.util.List;

public class Strong extends Paragraph {
	private final static String DOTS = "~";
    Strong(List<Markup> components) {
        super(components);
    }

    public void toMarkdown(StringBuilder resultingString) {
    	resultingString.append(DOTS);
        super.toMarkdown(resultingString);
        resultingString.append(DOTS);
    }
}