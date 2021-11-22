# ClassRegistrationDjango
Final Project CISC359 Fall 2021


Different parts of the project and the assigned person:

Front-end: Jon
Back-end: Mame
DB and Back-End: Cindy

Different tasks to discuss/complete


Database/Model requirements:

Student: StudentID(PK), FirstName, LastName, DateOfBirth, Major, ListOfCompletedClasses)
Transcript: EntryID(PK, hidden), StudentID(Foreign Key), Grade  
Major: MajorID(PK), MajorRequiredClasses  
Class: ClassID(PK), ClassSubject, ClassPrereqs, ClassCredits  


Sign Up   
    -- Screen  
    -- Needs Name(text entry), major(from list), Date of Birth(from calendar)  
    -- Add time of sign-up to model  
    -- Check if email already used  


Login   
    -- SCREEN  
    -- Accounts (Model and DB)  
    -- Make view based on Login  

Student landing page      
    -- Show registered classes if already registered  
    -- Show registering screen if not registered  

Register page   
    -- Show all classes  
    -- Option to filter classes  
    -- "shopping cart" system for classes, check out to register selected classes  
    -- Make sure prereqs are completed before registering  



Transcript Page?

    