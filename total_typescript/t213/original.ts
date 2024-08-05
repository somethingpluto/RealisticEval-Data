class Stack{
    private stack:number[] = [];

    public push(a: number): void
    {
        // add item to end of stack
        this.stack[this.stack.length] = a;
    }

    public pop(): number
    {
        // delete last element in stack
        const temp = this.stack[this.stack.length - 1];
        this.stack.splice(this.stack.length - 1, 1);
        return temp;
    }

    public isEmpty(): boolean
    {
        return this.stack.length === 0;
    }

    public peek(): number
    {
        // return last element of stack
        return this.stack[this.stack.length - 1 != -1 ? this.stack.length - 1 : 0];
    }
}
