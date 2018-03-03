package com.nyancake.pack_1.markup;

import java.util.List;

public class Emphasis extends Paragraph {
	private final static String DOTS = "*";
    Emphasis(List<Markup> elements) {
        super(elements);
    }

    public void toMarkdown(StringBuilder resultingString) {
    	resultingString.append(DOTS);
        super.toMarkdown(resultingString);
        resultingString.append(DOTS);
    }
}