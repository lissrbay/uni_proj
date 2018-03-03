package com.nyancake.pack_1.markup;

import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args){
        Paragraph paragraph = new Paragraph(Collections.singletonList(
                new Strong(Arrays.asList(
                        new Text("1"),
                        new Strikeout(Arrays.asList(
                                new Text("2"),
                                new Emphasis(Arrays.asList(
                                        new Text("3"),
                                        new Text("4"))),
                                new Text("5")
                        )),
                        new Text("6")
                ))
        ));
        StringBuilder resultingString = new StringBuilder();
        paragraph.toMarkdown(resultingString);
        System.out.print(resultingString);
    }
}