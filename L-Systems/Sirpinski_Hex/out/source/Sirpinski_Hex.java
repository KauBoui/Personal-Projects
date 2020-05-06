import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Sirpinski_Hex extends PApplet {


String axiom = "f";
String sentence = axiom;
int len = 50;
float theta = 0;

char[] rules_key = {'f', 'h'};


String[] rules_replace = {"h-f-h", "f+h+f"};



public void generate()
{
    String nextSentence = "";
    len *= 0.85f;
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
    translate(width,height);
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
    theta = radians(60);
    
}

public void draw()
{
    if (keyPressed == true){
        generate();
    }
}
  public void settings() {  size(1000, 1000); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Sirpinski_Hex" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
