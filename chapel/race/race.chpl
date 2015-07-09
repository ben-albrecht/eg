// Chapel toy program to have processors race to complete a task

module race {
    proc foo() {
      writeln("This is the race program");
    }

}


proc main() {
    use race;
    foo();
}
