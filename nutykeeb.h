#ifndef NUTYKEEBHPP
#define NUTYKEEBHPP

class ButtonRegister{
  public:
  bool pressed;
};

#define MATRIX_MAX_SIZE  8

class ButtonMatrix{
    private:
      ButtonRegister m_buttons[ MATRIX_MAX_SIZE ][ MATRIX_MAX_SIZE ] ;
    
    public:
      ButtonMatrix();
      inline ButtonRegister& button(int row, int column){
        return m_buttons[row][column];
      }

};

#endif //NUTYKEEBHPP

