
String axiom = "f";
String sentence = axiom;
int len = 100;
float theta = 0;


char[] rules_key = {'f'};


String[] rules_replace = {"f[+f]f[-f]f"};



void generate()
{
    String nextSentence = "";
    len *= 0.5;
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
    theta = radians(25.7);
    size(1000, 1000);
}

void draw()
{
    if (keyPressed == true){
        generate();
    }
}
