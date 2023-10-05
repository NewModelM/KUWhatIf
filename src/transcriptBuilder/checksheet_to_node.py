"""
Connor Morgandale
Node Information
• A node is a specific requirement on a checksheet (such as required courses)
• Using a class with functions which can make both a list of classes and a list of options the nodes can be dynamic
Node Name{
	int CreditsRequired
	#Courses that need to be taken
	list<string> RequiredCourses ["", "CSC 315", "APD 104", etc.]
	# Courses with options: <name> [first element of the list <number of required credits>,…]    ex. Natural Science Course for a Science Major (NAT SCI)
	list<string> NatSciCourses ["3", "GEO 100", etc.]
} 
"""
