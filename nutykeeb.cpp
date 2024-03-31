#include "nutykeeb.h"



ButtonMatrix::ButtonMatrix(){
  for(int c = 0; c<MATRIX_MAX_SIZE; c++){
    for(int r = 0; r<MATRIX_MAX_SIZE; r++){
      button(r, c).pressed = false;
    }

  }
}