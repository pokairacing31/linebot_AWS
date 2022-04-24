import csv

from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer


class Menu():
    def datas(self):
        path = 'gooder.csv'
        with open(path, newline='',encoding='UTF-8') as csvfile :
            rows = csv.reader(csvfile)
            datas =list(rows)
        return datas

    def menu_add(self):
        datas = self.datas()
        menu_list=[]
        for data in datas:
            a = [data[0], data[1]]
            if a not in menu_list:
                menu_list.append(a)
        print(menu_list)
        return menu_list

    def buttom(self):
        menu_list = self.menu_add()
        buttom_list=[]
        for menu in menu_list:
            buttom_list.append(
                ButtonComponent(
                action=PostbackAction(
                label = menu[0],
                data = menu[1]
                ),
                height='md',
                color='#3CA0DC',
                style='primary',
                margin = 'xs'
            ))
        return buttom_list
        
    def get_menu_flex_message(self):
        buttom_list = self.buttom()
        flex_message_card = BubbleContainer(
                size='kilo',
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        TextComponent(
                            text='常見問題',
                            size='xl',
                            weight='bold'
                        )]
                ),
                footer=BoxComponent(
                    layout='vertical',
                    contents=buttom_list,
                    position='relative'
                ),
                styles={
                    'header': BlockStyle(separator=False),
                    'body': BlockStyle(Separator=True),
                    'footer': BlockStyle(Separator=False)
                }
            )
            
        
        #print(flex_message_card)
        return flex_message_card
    def is_Menu(self, text):
            return True if '常見問題' in text else False
