
class TaskItem(object):
    def __init__(self, taskitem: str):
        self.taskitem = taskitem

    def __str__(self):
        return self.taskitem

    def __repr__(self):
        return self.taskitem

    def get_taskitem(self) -> str:
        """
        This will return the taskitem as string
        Returns:
        str: taskitem as string
        """
        return self.taskitem

    def set_taskitem(self, taskitem: str):
        """
        This will set the taskitem as string
        Args:
            taskitem:

        Returns: None
        """
        self.taskitem = taskitem

