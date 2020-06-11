import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.Random; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class StochasticLSystems extends PApplet {

 

String axiom = "f";
String sentence = axiom;
int len = 300;
float theta = 0;




public void generate()
{
    String nextSentence = "";
    len *= 0.5f;
    for (int i = 0; i < sentence.length(); i++)
    {
        char current = sentence.charAt(i);
        float rand = random(0, 1);
        if (current == 'f')
        {
            if (rand < 0.33f)
            {
                nextSentence += "f[+f]f[-f]f";
            } else if (rand > 0.66f) {
                nextSentence += "f[+f]f";
            } else if (rand > 0.33f && rand < 0.66f) {
                nextSentence += "f[-f]f";
            } 
        } else {
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
    theta = radians(25);
    
}

public void draw()
{
    if (keyPressed == true){
        generate();
    }
}
  public void settings() {  size(1000, 1000); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "StochasticLSystems" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
