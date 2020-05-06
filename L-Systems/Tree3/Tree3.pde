
String axiom = "ff";
String sentence = axiom;
int len = 100;
float theta = 0;

char[] rules_key = {'f', '+', '-'};

String[] rules_replace_1 = {"+[f+ff+f]-[f-ff-f]", "f+f", "f-f"};
String[] rules_replace_2 = {"-[f+ff-f]+[f-ff+f]", "f+f", "f-f"};



void generate()
{
    String nextSentence = "";
    len *= 0.5;
    for (int i = 0; i < sentence.length(); i++)
    {
        char current = sentence.charAt(i);
        boolean found = false;
        float rand = random(0, 1);
        for (int j = 0; j < rules_key.length; j++)
        {
            if (current == rules_key[j])
            {
                if (rand < 0.5)
                {
                    nextSentence += rules_replace_1[j];
                    found = true;
                    break;
                } else {
                nextSentence += rules_replace_2[j];
                found = true;
                break;
                }
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
    translate(width / 2 , height);
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
