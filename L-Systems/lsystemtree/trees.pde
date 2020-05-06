ArrayList<Tree> trees = new ArrayList<Tree>();

void setup()
{
  size(1920, 1080);
}



void draw()
{
  background(175,247,237);
  for (int i=0; i<trees.size(); i++) {
    Tree t = trees.get(i);
    push();
    t.generate();
    pop();
  }
}

void mouseClicked() {
  trees.add(new Tree(mouseX, mouseY));
}
