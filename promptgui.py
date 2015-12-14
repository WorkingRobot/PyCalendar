def start():
    # IMPORTS BELOW #
    import pygame
    # IMPORTS ABOVE #

    # CREATE scr BELOW #
    pygame.init()
    scr_w = 500
    scr_h = 150
    scr = pygame.display.set_mode([scr_w, scr_h])
    # CREATE scr ABOVE #

    # COLORS BELOW #
    black = (000,000,000)
    white = (255,255,255)
    red   = (255,000,000)
    blue  = (000,000,255)
    green = (000,255,000)
    # COLORS ABOVE #

    # CAPTIONS BELOW #
    '''pygame.display.set_icon(pygame.image.load("Img").convert_alpha())'''
    # CAPTIONS ABOVE #

    # IMAGES BELOW #

    # IMAGES ABOVE #

    # LOOP PREP BELOW #
    done=False
    clock = pygame.time.Clock()
    text = ""
    # LOOP PREP ABOVE #

    # FUNCTIONS BELOW #
    def typetext(font, size, text, x, y, alias, color, upside):
        defined_font = pygame.font.Font(font, size)
        stamp = defined_font.render(text, alias, color)
        if upside:
            stamp = pygame.transform.flip(stamp, False, True)
        scr.blit(stamp, [x,y])
    # FUNCTIONS ABOVE #

    #######################################################################
    ############################## MAIN LOOP ##############################
    #######################################################################

    while not done:
        # EVENTS BELOW #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    return text
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    if event.key == pygame.K_a:
                        text += 'A'
                    elif event.key == pygame.K_b:
                        text += 'B'
                    elif event.key == pygame.K_c:
                        text += 'C'
                    elif event.key == pygame.K_d:
                        text += 'D'
                    elif event.key == pygame.K_e:
                        text += 'E'
                    elif event.key == pygame.K_f:
                        text += 'F'
                    elif event.key == pygame.K_g:
                        text += 'G'
                    elif event.key == pygame.K_h:
                        text += 'H'
                    elif event.key == pygame.K_i:
                        text += 'I'
                    elif event.key == pygame.K_j:
                        text += 'J'
                    elif event.key == pygame.K_k:
                        text += 'K'
                    elif event.key == pygame.K_l:
                        text += 'L'
                    elif event.key == pygame.K_m:
                        text += 'M'
                    elif event.key == pygame.K_n:
                        text += 'N'
                    elif event.key == pygame.K_o:
                        text += 'O'
                    elif event.key == pygame.K_p:
                        text += 'P'
                    elif event.key == pygame.K_q:
                        text += 'Q'
                    elif event.key == pygame.K_r:
                        text += 'R'
                    elif event.key == pygame.K_s:
                        text += 'S'
                    elif event.key == pygame.K_t:
                        text += 'T'
                    elif event.key == pygame.K_u:
                        text += 'U'
                    elif event.key == pygame.K_v:
                        text += 'V'
                    elif event.key == pygame.K_w:
                        text += 'W'
                    elif event.key == pygame.K_x:
                        text += 'X'
                    elif event.key == pygame.K_y:
                        text += 'Y'
                    elif event.key == pygame.K_z:
                        text += 'Z'
                elif not(event.key == pygame.K_LSHIFT) or not(event.key == pygame.K_RSHIFT):
                    if event.key == pygame.K_a:
                        text += 'a'
                    elif event.key == pygame.K_b:
                        text += 'b'
                    elif event.key == pygame.K_c:
                        text += 'c'
                    elif event.key == pygame.K_d:
                        text += 'd'
                    elif event.key == pygame.K_e:
                        text += 'e'
                    elif event.key == pygame.K_f:
                        text += 'f'
                    elif event.key == pygame.K_g:
                        text += 'g'
                    elif event.key == pygame.K_h:
                        text += 'h'
                    elif event.key == pygame.K_i:
                        text += 'i'
                    elif event.key == pygame.K_j:
                        text += 'j'
                    elif event.key == pygame.K_k:
                        text += 'k'
                    elif event.key == pygame.K_l:
                        text += 'l'
                    elif event.key == pygame.K_m:
                        text += 'm'
                    elif event.key == pygame.K_n:
                        text += 'n'
                    elif event.key == pygame.K_o:
                        text += 'o'
                    elif event.key == pygame.K_p:
                        text += 'p'
                    elif event.key == pygame.K_q:
                        text += 'q'
                    elif event.key == pygame.K_r:
                        text += 'r'
                    elif event.key == pygame.K_s:
                        text += 's'
                    elif event.key == pygame.K_t:
                        text += 't'
                    elif event.key == pygame.K_u:
                        text += 'u'
                    elif event.key == pygame.K_v:
                        text += 'v'
                    elif event.key == pygame.K_w:
                        text += 'w'
                    elif event.key == pygame.K_x:
                        text += 'x'
                    elif event.key == pygame.K_y:
                        text += 'y'
                    elif event.key == pygame.K_z:
                        text += 'z'
                
                if keys[pygame.K_0] or keys[pygame.K_KP0]:
                    text += '0'
                elif keys[pygame.K_1] or keys[pygame.K_KP1]:
                    text += '1'
                elif keys[pygame.K_2] or keys[pygame.K_KP2]:
                    text += '2'
                elif keys[pygame.K_3] or keys[pygame.K_KP3]:
                    text += '3'
                elif keys[pygame.K_4] or keys[pygame.K_KP4]:
                    text += '4'
                elif keys[pygame.K_5] or keys[pygame.K_KP5]:
                    text += '5'
                elif keys[pygame.K_6] or keys[pygame.K_KP6]:
                    text += '6'
                elif keys[pygame.K_7] or keys[pygame.K_KP7]:
                    text += '7'
                elif keys[pygame.K_8] or keys[pygame.K_KP8]:
                    text += '8'
                elif keys[pygame.K_9] or keys[pygame.K_KP9]:
                    text += '9'
            '''elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass'''
        # EVENTS ABOVE #

        # LOGIC BELOW #
        
        # LOGIC ABOVE #
        
        scr.fill(white)
        
        # DRAWING BELOW #
        typetext("guitext.TTF", 100, text, 20, 20, True, black, False)
        # DRAWING ABOVE #
        
        pygame.display.flip()
        
        # LOOP RESTART PREP BELOW #
        clock.tick(60)
        # LOOP RESTART PREP ABOVE #

    pygame.quit()
