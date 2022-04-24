import csv
from webbrowser import get
from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer
from menu import Menu
class FAQ():
    def datas(self):
        path = 'gooder.csv'
        with open(path, newline='',encoding='UTF-8') as csvfile :
            rows = csv.reader(csvfile)
            datas =list(rows)
        return datas
    
    def get_return_from_menu(self,code):
        datas = self.datas()
        ques_list = []
        for data in datas:
            if data[1] == code:
                ques = [data[2],data[3],data[4]]
                ques_list.append(ques)
        return ques_list
    def buttoms(self):
        ques_list = self.get_return_from_menu()
        buttoms_list=[]
        for bottom in ques_list:
            buttoms_list.append(
                ButtonComponent(
                action=PostbackAction(
                label = bottom[1],
                data = bottom[0]
                ),
                height='md',
                color='#3CA0DC',
                style='primary',
                margin = 'xs'
            )
            )
        return buttoms_list

    def Faq_flex_message(self,code):
        datas = self.datas()
        buttom_list=self.buttoms()
        flex_message_card = BubbleContainer(
                size='kilo',
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        TextComponent(
                            text=datas[code][0],
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
        return flex_message_card
    def answers(self,code):
        ques_list = self.get_return_from_menu()
        for ques in ques_list:
            if code == ques[0]:
                return ques_list[2]

        
    def is_faq(self,code):
        get_returns = self.datas()
        for get_return in get_returns:
            if code == get_return[1]:
                return True
            else:
                return False 
    def is_ans(self,code):
        get_returns = self.datas()
        for get_return in get_returns:
            if code == get_return[2]:
                return True
            else:
                return False

