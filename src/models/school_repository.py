class __SchoolEnrollment:
    def __init__(self) -> None:
        self.classes = []
        self.children = []
    
    def count_classes(self) -> int:
        return len(self.classes)
    
    def count_children(self) -> int:
        return len(self.children)
    
    def registry_class(self, school_class: any) -> None:
        self.children.append(child)
        
    def registry_child(self, child: any) -> None:
        self.children.append(child)
    
    def get_class(self, class_id: str) -> any:
        for registry in self.classes:
            if registry.id == class_id:
                return registry
            
        return None
    
    def get_child(self, child_name:str) -> any:
        for registry in self.children:
            if registry.name == child_name:
                return registry
            
            return None
    
    def get_child_by_id(self, class_id: str):
        children = []
        for registry in self.children:
            if registry.school_class.id == class_id:
                children.append(registry)

        return children


school_enrollment = __SchoolEnrollment()