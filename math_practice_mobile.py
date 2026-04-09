import random
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

class MathPracticeApp(App):
    def build(self):
        Window.size = (dp(360), dp(640))
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        return self.sm

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.difficulty = 1
        self.num_questions = 5
        self.create_main_layout()
    
    def create_main_layout(self):
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        with layout.canvas.before:
            Color(0.94, 0.97, 1, 1)  # #f0f8ff
            self.rect = Rectangle(pos=layout.pos, size=layout.size)
            layout.bind(pos=self.update_rect, size=self.update_rect)
        
        # 标题
        title = Label(
            text='一年级数学练习', 
            font_size=dp(24), 
            color=(0.29, 0.43, 0.65, 1),
            size_hint_y=None,
            height=dp(50)
        )
        layout.add_widget(title)
        
        # 装饰元素
        decoration = Label(
            text='快乐学习', 
            font_size=dp(18), 
            color=(1, 0.42, 0.42, 1),
            size_hint_y=None,
            height=dp(40)
        )
        layout.add_widget(decoration)
        
        # 难度选择
        difficulty_label = Label(
            text='选择难度:', 
            font_size=dp(18), 
            color=(0.29, 0.29, 0.29, 1),
            size_hint_y=None,
            height=dp(40),
            halign='left'
        )
        difficulty_label.bind(size=difficulty_label.setter('text_size'))
        layout.add_widget(difficulty_label)
        
        difficulty_layout = BoxLayout(orientation='horizontal', spacing=dp(20), size_hint_y=None, height=dp(60))
        
        self.difficulty_10 = Button(
            text='10以内', 
            font_size=dp(16), 
            background_color=(0.29, 0.43, 0.65, 1),
            color=(1, 1, 1, 1)
        )
        self.difficulty_10.bind(on_press=self.set_difficulty_10)
        
        self.difficulty_20 = Button(
            text='20以内', 
            font_size=dp(16), 
            background_color=(0.62, 0.62, 0.62, 1),
            color=(1, 1, 1, 1)
        )
        self.difficulty_20.bind(on_press=self.set_difficulty_20)
        
        difficulty_layout.add_widget(self.difficulty_10)
        difficulty_layout.add_widget(self.difficulty_20)
        layout.add_widget(difficulty_layout)
        
        # 题目数量
        num_label = Label(
            text='题目数量:', 
            font_size=dp(18), 
            color=(0.29, 0.29, 0.29, 1),
            size_hint_y=None,
            height=dp(40),
            halign='left'
        )
        num_label.bind(size=num_label.setter('text_size'))
        layout.add_widget(num_label)
        
        self.num_entry = TextInput(
            text='5', 
            font_size=dp(18), 
            size_hint=(1, None), 
            height=dp(50),
            multiline=False,
            input_filter='int'
        )
        layout.add_widget(self.num_entry)
        
        # 开始按钮
        start_button = Button(
            text='开始练习', 
            font_size=dp(20), 
            background_color=(0.29, 0.43, 0.65, 1), 
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(60)
        )
        start_button.bind(on_press=self.start_practice)
        layout.add_widget(start_button)
        
        self.add_widget(layout)
    
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def set_difficulty_10(self, instance):
        self.difficulty = 1
        self.difficulty_10.background_color = (0.29, 0.43, 0.65, 1)
        self.difficulty_20.background_color = (0.62, 0.62, 0.62, 1)
    
    def set_difficulty_20(self, instance):
        self.difficulty = 2
        self.difficulty_20.background_color = (0.29, 0.43, 0.65, 1)
        self.difficulty_10.background_color = (0.62, 0.62, 0.62, 1)
    
    def start_practice(self, instance):
        try:
            self.num_questions = int(self.num_entry.text)
            if self.num_questions <= 0:
                self.show_popup('错误', '题目数量必须为正整数')
                return
        except ValueError:
            self.show_popup('错误', '请输入正确的数字')
            return
        
        # 生成题目
        questions = []
        for _ in range(self.num_questions):
            questions.append(self.generate_question(self.difficulty))
        
        # 切换到练习界面
        practice_screen = PracticeScreen(
            name='practice', 
            questions=questions, 
            num_questions=self.num_questions,
            main_screen=self
        )
        self.manager.add_widget(practice_screen)
        self.manager.current = 'practice'
    
    def generate_question(self, difficulty):
        max_result = 10 if difficulty == 1 else 20
        
        while True:
            operation = random.choice(['+', '-'])
            
            if operation == '+':
                num1 = random.randint(1, max_result - 1)
                num2 = random.randint(1, max_result - num1)
                answer = num1 + num2
            else:
                num2 = random.randint(1, max_result - 1)
                num1 = random.randint(num2, max_result)
                answer = num1 - num2
            
            if 0 < answer <= max_result:
                break
        
        return num1, operation, num2, answer
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title, 
            content=Label(text=message, font_size=dp(16)), 
            size_hint=(0.8, 0.3)
        )
        popup.open()

class PracticeScreen(Screen):
    def __init__(self, questions, num_questions, main_screen, **kwargs):
        super(PracticeScreen, self).__init__(**kwargs)
        self.questions = questions
        self.num_questions = num_questions
        self.main_screen = main_screen
        self.current_question = 0
        self.correct_count = 0
        self.user_answers = []
        self.start_time = 0
        self.total_time = 0
        self.create_practice_layout()
    
    def create_practice_layout(self):
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        with layout.canvas.before:
            Color(0.94, 0.97, 1, 1)  # #f0f8ff
            self.rect = Rectangle(pos=layout.pos, size=layout.size)
            layout.bind(pos=self.update_rect, size=self.update_rect)
        
        # 进度信息
        self.progress_label = Label(
            text=f'进度: 0/{self.num_questions}', 
            font_size=dp(18), 
            color=(0.29, 0.29, 0.29, 1),
            size_hint_y=None,
            height=dp(40)
        )
        layout.add_widget(self.progress_label)
        
        # 题目信息
        self.question_label = Label(
            text='', 
            font_size=dp(28), 
            color=(0.29, 0.43, 0.65, 1),
            size_hint_y=None,
            height=dp(80)
        )
        layout.add_widget(self.question_label)
        
        # 答案输入
        answer_label = Label(
            text='答案:', 
            font_size=dp(18), 
            color=(0.29, 0.29, 0.29, 1),
            size_hint_y=None,
            height=dp(40),
            halign='left'
        )
        answer_label.bind(size=answer_label.setter('text_size'))
        layout.add_widget(answer_label)
        
        self.answer_entry = TextInput(
            font_size=dp(20), 
            size_hint=(1, None), 
            height=dp(60),
            multiline=False,
            input_filter='int'
        )
        layout.add_widget(self.answer_entry)
        
        # 按钮框架
        button_layout = BoxLayout(orientation='horizontal', spacing=dp(15), size_hint_y=None, height=dp(60))
        
        # 提交按钮
        submit_button = Button(
            text='提交答案', 
            font_size=dp(18), 
            background_color=(0.29, 0.43, 0.65, 1), 
            color=(1, 1, 1, 1)
        )
        submit_button.bind(on_press=self.check_answer)
        button_layout.add_widget(submit_button)
        
        # 返回按钮
        back_button = Button(
            text='返回', 
            font_size=dp(18), 
            background_color=(0.62, 0.62, 0.62, 1), 
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_press=self.confirm_exit)
        button_layout.add_widget(back_button)
        
        layout.add_widget(button_layout)
        self.add_widget(layout)
        self.show_next_question()
    
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def show_next_question(self):
        if self.current_question < self.num_questions:
            self.progress_label.text = f'进度: {self.current_question}/{self.num_questions}'
            num1, operation, num2, _ = self.questions[self.current_question]
            self.question_label.text = f'第{self.current_question+1}题: {num1} {operation} {num2} = ?'
            self.answer_entry.text = ''
            self.answer_entry.focus = True
            self.start_time = time.time()
        else:
            self.progress_label.text = f'进度: {self.num_questions}/{self.num_questions}'
            self.show_result()
    
    def check_answer(self, instance):
        elapsed_time = time.time() - self.start_time
        self.total_time += elapsed_time
        
        try:
            user_answer = int(self.answer_entry.text)
        except ValueError:
            self.show_popup('错误', '请输入正确的数字')
            return
        
        num1, operation, num2, correct_answer = self.questions[self.current_question]
        self.user_answers.append((num1, operation, num2, correct_answer, user_answer))
        
        if user_answer == correct_answer:
            self.show_popup('结果', '正确！')
            self.correct_count += 1
            self.current_question += 1
            self.show_next_question()
        else:
            self.show_popup('结果', f'错误，正确答案是: {correct_answer}')
            self.current_question += 1
            self.show_next_question()
    
    def confirm_exit(self, instance):
        # 创建确认弹窗
        content = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))
        message = Label(
            text='确定要结束当前练习吗？\n已完成的题目将不会保存。',
            font_size=dp(16),
            halign='center'
        )
        message.bind(size=message.setter('text_size'))
        content.add_widget(message)
        
        button_layout = BoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(50))
        
        cancel_button = Button(
            text='取消',
            font_size=dp(16),
            background_color=(0.62, 0.62, 0.62, 1),
            color=(1, 1, 1, 1)
        )
        cancel_button.bind(on_press=lambda x: popup.dismiss())
        button_layout.add_widget(cancel_button)
        
        confirm_button = Button(
            text='确定',
            font_size=dp(16),
            background_color=(0.96, 0.26, 0.21, 1),
            color=(1, 1, 1, 1)
        )
        confirm_button.bind(on_press=lambda x: self.exit_practice(popup))
        button_layout.add_widget(confirm_button)
        
        content.add_widget(button_layout)
        
        popup = Popup(
            title='确认',
            content=content,
            size_hint=(0.85, 0.35)
        )
        popup.open()
    
    def exit_practice(self, popup):
        popup.dismiss()
        self.user_answers = []
        self.total_time = 0
        self.manager.current = 'main'
        self.manager.remove_widget(self)
    
    def show_result(self):
        accuracy = (self.correct_count / self.num_questions) * 100
        
        if self.correct_count == self.num_questions:
            encouragement = '太棒了！全部正确，你是数学小天才！'
            encouragement_color = (0.3, 0.68, 0.3, 1)
        elif accuracy >= 80:
            encouragement = '做得很好！继续加油！'
            encouragement_color = (0.3, 0.68, 0.3, 1)
        elif accuracy >= 60:
            encouragement = '不错！再努力一下就能做得更好！'
            encouragement_color = (1, 0.6, 0, 1)
        else:
            encouragement = '别灰心，多练习就会进步的！'
            encouragement_color = (0.95, 0.27, 0.22, 1)
        
        # 创建结果弹窗
        result_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))
        
        with result_layout.canvas.before:
            Color(0.94, 0.97, 1, 1)  # #f0f8ff
            self.result_rect = Rectangle(pos=result_layout.pos, size=result_layout.size)
            result_layout.bind(pos=self.update_result_rect, size=self.update_result_rect)
        
        # 标题
        title = Label(
            text='练习完成！',
            font_size=dp(22),
            color=(0.29, 0.43, 0.65, 1),
            size_hint_y=None,
            height=dp(40)
        )
        result_layout.add_widget(title)
        
        # 结果信息
        info_layout = BoxLayout(orientation='vertical', spacing=dp(5), size_hint_y=None, height=dp(120))
        
        info_layout.add_widget(Label(text=f'共{self.num_questions}道题', font_size=dp(16), color=(0.29, 0.29, 0.29, 1)))
        info_layout.add_widget(Label(text=f'答对{self.correct_count}道', font_size=dp(16), color=(0.29, 0.29, 0.29, 1)))
        info_layout.add_widget(Label(text=f'正确率: {accuracy:.1f}%', font_size=dp(16), color=(0.29, 0.29, 0.29, 1)))
        info_layout.add_widget(Label(text=f'总用时: {self.total_time:.1f}秒', font_size=dp(16), color=(0.29, 0.29, 0.29, 1)))
        
        result_layout.add_widget(info_layout)
        
        # 鼓励信息
        encouragement_label = Label(
            text=encouragement,
            font_size=dp(18),
            color=encouragement_color,
            size_hint_y=None,
            height=dp(50),
            halign='center'
        )
        encouragement_label.bind(size=encouragement_label.setter('text_size'))
        result_layout.add_widget(encouragement_label)
        
        # 返回主界面按钮
        back_button = Button(
            text='返回主界面',
            font_size=dp(18),
            background_color=(0.29, 0.43, 0.65, 1),
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(60)
        )
        back_button.bind(on_press=self.back_to_main)
        result_layout.add_widget(back_button)
        
        # 题目记录标题
        record_label = Label(
            text='练习记录',
            font_size=dp(18),
            color=(0.29, 0.43, 0.65, 1),
            size_hint_y=None,
            height=dp(40)
        )
        result_layout.add_widget(record_label)
        
        # 创建滚动视图
        scroll_view = ScrollView(size_hint=(1, 1))
        
        # 创建记录列表
        record_layout = BoxLayout(orientation='vertical', spacing=dp(5), size_hint_y=None)
        record_layout.bind(minimum_height=record_layout.setter('height'))
        
        # 添加题目记录
        for i, (num1, operation, num2, correct_answer, user_answer) in enumerate(self.user_answers, 1):
            is_correct = user_answer == correct_answer
            status = '✓' if is_correct else '✗'
            status_color = (0.3, 0.68, 0.3, 1) if is_correct else (0.95, 0.27, 0.22, 1)
            
            record_text = f'第{i:2d}题: {num1:2d} {operation} {num2:2d} = {correct_answer:2d}  你的答案: {user_answer:2d}  {status}'
            record_label = Label(
                text=record_text,
                font_size=dp(14),
                color=status_color,
                size_hint_y=None,
                height=dp(35),
                halign='left'
            )
            record_label.bind(size=record_label.setter('text_size'))
            record_layout.add_widget(record_label)
        
        scroll_view.add_widget(record_layout)
        result_layout.add_widget(scroll_view)
        
        # 创建弹窗
        popup = Popup(
            title='练习结果',
            content=result_layout,
            size_hint=(0.95, 0.95)
        )
        popup.open()
    
    def update_result_rect(self, instance, value):
        self.result_rect.pos = instance.pos
        self.result_rect.size = instance.size
    
    def back_to_main(self, instance):
        self.user_answers = []
        self.total_time = 0
        self.manager.current = 'main'
        self.manager.remove_widget(self)
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title, 
            content=Label(text=message, font_size=dp(16)), 
            size_hint=(0.8, 0.3)
        )
        popup.open()

if __name__ == '__main__':
    MathPracticeApp().run()