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

public class Multi_Tree extends PApplet {

ArrayList<Tree> trees = new ArrayList<Tree>();

public void setup()
{
  
}



public void draw()
{
  background(175,247,237);
  for (int i=0; i<trees.size(); i++) {
    Tree t = trees.get(i);
    push();
    t.generate();
    pop();
  }
}

public void mouseClicked() {
  trees.add(new Tree(mouseX, mouseY));
}
 



class Tree
{
  String axiom;
  String sentence;
  int len;
  float theta;
  float positionx;
  float positiony;

  Tree(float px, float py)
  {
    axiom = "f";
    sentence = axiom;
    len = 300;
    theta = radians(20);
    positionx = px;
    positiony = py;
  }

  public void generate()
  {
    // skip straight to turtle if too long
    if (sentence.length()<1000) {
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
                nextSentence += "f[+fa]f[-fa]f";
            } else if (rand > 0.66f) {
                nextSentence += "f[+fa]f";
            } else if (rand > 0.33f && rand < 0.66f) {
                nextSentence += "f[-fa]f";
            } 
        } else { nextSentence += current; }
        sentence = nextSentence;
        }
        turtle(positionx, positiony);
    }
  }
  public void turtle(float p1, float p2)
  {
    resetMatrix();
    translate(p1, p2);
    stroke(255);
    strokeWeight(3);
    for (int i = 0; i < sentence.length(); i++)
    {
      char current = sentence.charAt(i);
      
     if (current == 'f'){
        line(0, 0, 0, -len);
        translate(0, - len);
      } else if (current == '+') {
          rotate(theta);
      } else if (current == '-') {
          rotate(-theta);
      } else if (current == '[') {
          push();
      } else if (current == ']') {
          pop();
      }
        else if (current == 'a') {
          noStroke();
          float rand = random(0, 1); 
          if (rand < 0.33f)
          {
            fill(99, 10, 106, 100);
          }
          else if (rand >= 0.66f)
          {
            fill(240, 128, 208, 100);
          }
          
          else
          {
            fill(32, 103, 17, 100);
          }
          ellipse(0,0,8, 20);
          stroke(255);
     }
    }
  }
}
  public void settings() {  size(1920, 1080); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Multi_Tree" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
