import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class In_Processing extends PApplet {



String axiom = "f";
String sentence = axiom;
int len = 100;
float theta = 0;


char[] rules_key = {'f'};


String[] rules_replace = {"f[+f]f[-f]f"};



public void generate()
{
    String nextSentence = "";
    len *= 0.5f;
    for (int i = 0; i < sentence.length(); i++)
    {
        char current = sentence.charAt(i);
        boolean found = false;
        for (int j = 0; j < rules_key.length; j++)
        {
            if (current == rules_key[j])
            {
                nextSentence += rules_replace[j];
                found = true;
                break;
            }
        }
        if (!found)
        {
            nextSentence += current;
        }
    }
    sentence = nextSentence;
    turtle();
    
}


public void turtle()
{
    background(51);
    resetMatrix();
    translate(width / 2, height);
    stroke(255);
    for (int i = 0; i < sentence.length(); i++)
    {
        char current = sentence.charAt(i);
        if (current == 'f')
        {
          line(0,0,0,-len);
          translate(0, - len);
        } else if (current == '+'){
          rotate(theta);
        } else if (current == '-'){
          rotate(-theta);
        } else if (current == '['){
          push();
        } else if (current == ']'){
          pop();
        }
    }
}

public void setup()
{
    theta = radians(25.7f);
    
}

public void draw()
{
    if (keyPressed == true){
        generate();
    }
}


// var axiom = "F";
// var sentence = axiom;
// var len = 100;
// var theta = 0;
// 
// var rules = [];
// rules[0] = 
// {
//   a: "F",
//   b: "FF+[+F-F-F]-[-F+F+F]"
// }
// 
// function generate()
// {
//   var nextSentence = "";
//   len *= 0.5;
//   for (var i = 0; i < sentence.length; i++)
//   {
//     var current = sentence.charAt(i);
//     var found = false;
//     for (var j = 0; j < rules.length; j++)
//     {
//       if (current == rules[j].a)
//       {
//         found = true;
//         nextSentence += rules[j].b;
//         break;
//       }
//     }
//     if (!found)
//     {
//       nextSentence += current; 
//     }
//   }
//   sentence = nextSentence;
//   createP(sentence);
//   turtle();
// }
// 
// function turtle()
// {
//   background(51);
//   resetMatrix();
//   translate(width / 2, height);
//   stroke(255);
//   for (var i = 0; i < sentence.length; i++)
//   {
//     var current = sentence.charAt(i);
//     if (current == "F")
//     {
//       line(0,0,0,-len);
//       translate(0, - len);
//     } else if (current == "+"){
//       rotate(theta);
//     } else if (current == "-"){
//       rotate(-theta);
//     } else if (current == "["){
//       push();
//     } else if (current == "]"){
//       pop();
//     }
//   }
// }
// 
// function setup() 
// {
//   theta = radians(25);
//   createCanvas(400, 400);
//   createP(axiom);
//   var button = createButton("generate");
//   button.mousePressed(generate);
// }
// 
// 
// 
// function draw() 
// {
//   
// }
  public void settings() {  size(1000, 1000); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "In_Processing" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
