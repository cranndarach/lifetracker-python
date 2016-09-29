#ifndef LOGCOPECH_H
#define LOGCOPECH_H

#include "entry.h"

class LogCopech: public Entry {
public:
    // explicit
    LogCopech(Entry *parent = 0);
    ~LogCopech(); // destructor
};


#endif // LOGCOPECH_H
