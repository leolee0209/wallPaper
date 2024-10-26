#include <iostream>
#include <Lilac.hpp>

using namespace std;

int main()
{
    LoggerInit("/home/leo/Desktop/projects/wallPaper/launch/log.txt", true);
    Limb::LWindow window;
    window.create();

    Limb::Root root(&window);
    Limb::Rect r = {10, 10, 300, 300};
    Limb::Label l(r, {200, 200, 50, 255});
    root.addSeed(&l);

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