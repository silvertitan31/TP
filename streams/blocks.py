'''StreamField'''

from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    '''Title and Text'''

    title = blocks.CharBlock(required=True, help_text="Add Your Title")
    text = blocks.CharBlock(required=True, help_text="Add Additional Text")

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = "edit"
        label = "Title and Text"


class RichTextBlock(blocks.RichTextBlock):
    '''Rich Text Block with all features'''

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Richtext Editing"


class LimitedRichTextBlock(blocks.RichTextBlock):
    '''Rich Text only with Subset'''

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = ['bold', 'italic', 'link']

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Basic Richtext Editing"



class SubjectModuleBlock(blocks.StructBlock):
    '''Page Chooser Block'''
    
    module_name =  blocks.PageChooserBlock(required="True",help_text="Select Module",can_choose_root=False)
    module_information = blocks.CharBlock(required=True, help_text="Add Module Information")
    
       
    class Meta:
        template = "streams/subject_module_block.html"
        icon = "doc-full"
        label = "Add Module Information"
        
       
       
class LessonBlock(blocks.RichTextBlock):
    '''Rich Text only with Subset used for lesson '''
    '''@TODO add chemistry and mathematics  specific functions '''

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = ['bold', 'italic', 'link', 'h4', 'ul', 'li','image']

    class Meta:
        label = "Section Content"      
        
        
class LessonContentBlock(blocks.StructBlock):
    '''Block containing Lesson Content. Each block will be wrapped ina section for css purposes'''
    
    title = blocks.CharBlock(required=True, label="Section Title",help_text="Add Section Title",max_length=40)
    text = LessonBlock(required=True, help_text="Add Section Content")


    class Meta:
        template = 'streams/lesson_content_block.html'
        icon = "doc-full"
        label = "Lesson Sections"
        help_text = "Each lesson section will cause  a link to be added to  sidebar for ease of navigation. Each section must have a title along with its content."


class QuizBlock(blocks.StructBlock):
    '''block containing question text, answer options, and answer as number'''
    question = blocks.RichTextBlock(required=True, label = "Question", help_text = "Add Question",)
    choice1 = blocks.RichTextBlock(required=True, label = "Choice 1", help_text = "Add Answer Choice 1",)
    choice2 = blocks.RichTextBlock(required=True, label = "Choice 2", help_text = "Add Answer Choice 2",)
    choice3 = blocks.RichTextBlock(required=True, label = "Choice 3", help_text = "Add Answer Choice 3",)
    choice4 = blocks.RichTextBlock(required=True, label = "Choice 4", help_text = "Add Answer Choice 4",)
    answer = blocks.IntegerBlock(min_value=1, max_value=4, required = True, label = "Answer Choice", help_text = "Enter the  answer number (1,2,3,4)")
    
    class Meta:
        label = "Quiz Questions"
        template = 'streams/quiz_block.html'
        icon = "doc-full"
  
    
    
    