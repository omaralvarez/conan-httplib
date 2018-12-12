//
//  Copyright (c) 2012 Yuji Hirose. All rights reserved.
//  The Boost Software License 1.0
//

#include <iostream>

#include <httplib/httplib.h>

using namespace httplib;

int main(void)
{
    Server svr;

    svr.Get("/hi", [](const Request& /*req*/, Response& res) {
        res.set_content("Hello World!", "text/plain");
    });

    std::cout << "Test OK!" << std::endl;

    //svr.listen("localhost", 1234);

    return 0;
}