#ifndef LOGGENERIC_H
#define LOGGENERIC_H

#include "entry.h"

class LogGeneric: public Entry {
public:
    // explicit
    LogGeneric(Entry *parent = 0);
    ~LogGeneric(); // destructor
};
#endif // LOGGENERIC_H
