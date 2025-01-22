#include <iostream>
#include <Lilac.hpp>
#include <filesystem>
#include <string>
using namespace std;
void run(){
    string path = std::filesystem::current_path();
    system(("bash " + path + "/../src/run.sh").c_str());
    // int startofsub = path.find("/wallPaper");
    // path = path.substr(0, startofsub + 10);
    // string mainPath = path + "/run/src/main.py";
    // string requirementPath = path + "/run/requirements.txt";

    // bool venv = std::filesystem::is_directory(path+"/run/venv");
    // if(!venv){
    //     system(("python3 -m venv " + path + "/run/venv").c_str());
    // }
    // system(("source " + path + "/run/venv/bin/activate").c_str());
    // system(("pip3 install -r " + requirementPath).c_str());
    // system(("python3 " + mainPath).c_str());
    // system("deactivate");
}
int main()
{
    string currentPath = std::filesystem::current_path();
    LoggerInit(currentPath.substr(0,currentPath.length() - 4) + "log.txt", true);
    Limb::LWindow window;
    window.create();

    Limb::Root root(&window);
    Limb::Rect r = {10, 10, 300, 300};
    Limb::Label l(r, {200, 200, 50, 255});

    Limb::Button runB({30, 30, 30, 30}, run);
    Limb::Label runL({0, 0, 30, 30}, {100, 100, 100, 255});
    root.addSeed(&l);
    root.addSeed(&runB);
    runB.addSeed(&runL);

    bool quit = false;
    while (!quit)
    {
        window.clear();
        root.draw();
        quit = Limb::interaction(&root);
        window.present();
    }
    window.close();
    return 0;
}