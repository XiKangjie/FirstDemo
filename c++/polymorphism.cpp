#include <iostream>
using namespace std;

class Base
{
private:
    int a;
public:
    virtual void PrintA() { cout << a << endl; }
};

class Derived : public Base
{
private:
    int b;
public:
    int c;

    Derived(): b(10), c(20) {}
    void PrintB()
    {
        cout << b << endl;
    }
};

int main()
{
    Base* pb = new Derived();
    //pb->Print();
    //cout << pb->c << endl;
    // 类Base至少要包含一个虚函数，才能转换成功。
    Derived* pd = dynamic_cast<Derived*>(pb);
    pd->PrintB();
    cout << pd->c << endl;

    return 0;
}

/*
#include <iostream>
#include <string>
using namespace std;

class IpsObjBase
{
public:
    virtual void Parse(std::string risk) = 0;
};

class SensitiveData : public IpsObjBase
{
public:
    int risk_level_;
public:
    virtual void Parse(std::string risk);
};

class FileFormat : public IpsObjBase
{
public:
    int risk_level_;
public:
    virtual void Parse(std::string risk);
};


void set_risk_level(IpsObjBase* pObj, std::string risk)
{
    if (risk == "high") {
        pObj->risk_level_ = 3;
    }
    else if (risk == "medium") {
        pObj->risk_level_ = 2;
    }
    else if (risk == "low") {
        pObj->risk_level_ = 1;
    }
}

void SensitiveData::Parse(std::string risk)
{
    set_risk_level(this, risk);
}

void FileFormat::Parse(std::string risk)
{
    set_risk_level(this, risk);
}

int main()
{
    SensitiveData sd;
    FileFormat ff;
    sd.Parse("high");
    ff.Parse("high");

    return 0;
}
*/
