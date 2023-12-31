import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kt_img = pg.image.load("ex01/fig/3.png") 
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_imgs =[kt_img, pg.transform.rotozoom(kt_img, 5, 1.0), pg.transform.rotozoom(kt_img, 10, 1.0), pg.transform.rotozoom(kt_img, 5, 1.0)]
    bg_imgs =[bg_img, pg.transform.flip(bg_img, True, False), bg_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

       
        tmr += 1
        x = tmr%3200

        
        for i in range(3):
            screen.blit(bg_imgs[i], [1600*i-x, 0])
        
        screen.blit(kt_imgs[tmr%4], [300, 200])



        pg.display.update()    
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()