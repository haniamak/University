class Reg64bit {
    Reg32bit reg1, reg2;
    
    read() {
        val = reg1;
        val += reg2 << 32;
        return val;
    }
    
    write(x) {
        reg1 = x % (1 << 32);
        reg2 = x >> 32;
    }
}