#ifndef LOGPAIN_H
#define LOGPAIN_H

#include "entry.h"

class LogPain: public Entry {
public:
    // explicit
    LogPain(Entry *parent = 0);
    ~LogPain(); // destructor
};


#endif // LOGPAIN_H
