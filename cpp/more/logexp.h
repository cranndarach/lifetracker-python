#ifndef LOGEXP_H
#define LOGEXP_H

#include "entry.h"

class LogExp: public Entry {
public:
    // explicit
    LogExp(Entry *parent = 0);
    ~LogExp(); // destructor
};
#endif // LOGEXP_H
