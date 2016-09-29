#ifndef LOGMOOD_H
#define LOGMOOD_H

#include "entry.h"

class LogMood: public Entry {
public:
    // explicit
    LogMood(Entry *parent = 0);
    ~LogMood(); // destructor
};


#endif // LOGMOOD_H
