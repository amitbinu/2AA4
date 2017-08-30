# Author:    	Amit Binu                  
# Revised:      Monday, Mar 20, 2017     
# Description: "makefile"                       

# Assumes JUnit is installed

JFLAGS = -g
JCLASS = -cp $(CLASSPATH):.:/usr/share/java/junit4.jar:/opt/local/share/java/hamcrest-core.jar
#JCLASS = -cp $(CLASSPATH):.:/usr/share/java/junit4.jar # on mills
JC = javac
JVM = java
.SUFFIXES: .java .class
.java.class:
        $(JC) $(JFLAGS) $(JCLASS) ./src/*.java

CLASSES = \
        *.java \

MAIN = TestPathCalculation

default: classes

classes: $(CLASSES:.java=.class)

test: $(MAIN).class
        $(JVM) $(JCLASS) org.junit.runner.JUnitCore $(MAIN)

clean:
        $(RM) *.class
