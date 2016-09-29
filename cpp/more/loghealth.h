#ifndef LOGHEALTH_H
#define LOGHEALTH_H

#include "entry.h"

class LogHealth: public Entry {
public:
    // explicit
    LogHealth(Entry *parent = 0);
    ~LogHealth(); // destructor
};


#endif // LOGHEALTH_H
