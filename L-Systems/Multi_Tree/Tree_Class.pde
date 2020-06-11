 import java.util.Random;



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

  void generate()
  {
    // skip straight to turtle if too long
    if (sentence.length()<1000) {
      String nextSentence = "";
      len *= 0.5;
      for (int i = 0; i < sentence.length(); i++)
      {
        char current = sentence.charAt(i);
        float rand = random(0, 1);
        if (current == 'f')
        {
            if (rand < 0.33)
            {
                nextSentence += "f[+fa]f[-fa]f";
            } else if (rand > 0.66) {
                nextSentence += "f[+fa]f";
            } else if (rand > 0.33 && rand < 0.66) {
                nextSentence += "f[-fa]f";
            } 
        } else { nextSentence += current; }
        sentence = nextSentence;
        }
        turtle(positionx, positiony);
    }
  }
  void turtle(float p1, float p2)
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
          if (rand < 0.33)
          {
            fill(99, 10, 106, 100);
          }
          else if (rand >= 0.66)
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
