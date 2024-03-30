#include "nutykeeb.h"



ButtonMatrix::ButtonMatrix(){
  for(int c = 0; c<8; c++){
    for(int r = 0; r<8; r++){
      button(r, c).pressed = false;
    }

  }
}