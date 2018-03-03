package com.nyancake.pack_1.markup;

import java.util.List;

public class Paragraph implements Markup {
    private List<Markup> components;
    Paragraph(){}
    Paragraph(List<Markup>elements){
        this.components = elements;
    }

    public void toMarkdown(StringBuilder resultingString) {
        for (int i = 0; i < components.size(); i++){
        	components.get(i).toMarkdown(resultingString);
        }
    }
}