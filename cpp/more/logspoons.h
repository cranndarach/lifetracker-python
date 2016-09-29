#ifndef LOGSPOONS_H
#define LOGSPOONS_H

#include "entry.h"

class LogSpoons: public Entry {
public:
    // explicit
    LogSpoons(Entry *parent = 0);
    ~LogSpoons(); // destructor
};


#endif // LOGSPOONS_H
