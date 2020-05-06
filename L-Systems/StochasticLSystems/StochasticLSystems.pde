 import java.util.Random;

String axiom = "f";
String sentence = axiom;
int len = 300;
float theta = 0;




void generate()
{
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
                nextSentence += "f[+f]f[-f]f";
            } else if (rand > 0.66) {
                nextSentence += "f[+f]f";
            } else if (rand > 0.33 && rand < 0.66) {
                nextSentence += "f[-f]f";
            } 
        } else {
            nextSentence += current;
        }
    }
    sentence = nextSentence;
    turtle();
}


void turtle()
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

void setup()
{
    theta = radians(25);
    size(1000, 1000);
}

void draw()
{
    if (keyPressed == true){
        generate();
    }
}