 ������ 10, ������� 13
 
  �������� ��������� "��������� ����������" ��� ����. ������������ ������ ���� ������������� 30 �������, 
  ������� ����� ������������ ����� �������� ����������������: ����, ��������, �������� � ��������. 
  ���� ������� ���, ����� ������������ ��� �� ������ ����� ��� ������ �� ������ "����",
 �� � ���������� �� ���� �� �������������, ������� �� ����� ��������� ������ ��������.
 
  
  
 
  ��������� �������� ����:
 MENU = ("""
 ������� ����:
    0. �����.
    1. �������� ����.
    2. ������ ����.
 � ��� ���� {} ����/-�� ��������.
    """)
  ��������� ����� � ���� �������:
 attribute_points = 30
 attributes = {"����": 0,
              "��������": 0,
              "��������": 0,
              "��������": 0,
             }
  ��������� - "���� ����������":
 STATS_MENU = ("""
���� ���������:
    0. ����� � ���������� ����.
     1. ���� = {0}
     2. �������� = {1}
     3. �������� = {2}
     4. �������� = {3}
 � ��� {4} ����/-�� ��������.
     """)
  ������ ���� ���������.
  ���������� ������������ ���������� � ������� ����.
 choise = ""
 while choise != "0":
     print(MENU.format(attribute_points))
      ������ ������������ ������� ������ �����.
     choise = input("������� ������ ��� ����� ����: ")
         
     ������������ ���� ������������.
     if choise == "0":
         print("��������� ���������") # ��� ����� �� ���������.
     elif choise == "1" or choise == "2":        
          ���������� ������������ ���������� � ���� "������ ����������".
         selected_attribute = ""            
         while selected_attribute != "0":
             ��� ����� �� ����� ������ ����:
             print(STATS_MENU.format(attributes["����"], attributes["��������"], attributes["��������"], attributes["��������"], attribute_points))
             selected_attribute = input("������� ����� ���������, ��� ��������� ��� \"0\", ��� ������: ")
            
            if selected_attribute == "1" or selected_attribute == "2" or selected_attribute == "3"\
                 or selected_attribute == "4" or selected_attribute == "0":
                 if selected_attribute == "0": # ������� � ���������� ����.
                     continue            
                  ��������� �������� ���������� ������ ����.    
                 elif selected_attribute == "1":
                     alterable_attribute = "����"
                 elif selected_attribute == "2":
                     alterable_attribute = "��������"
                 elif selected_attribute == "3":
                     alterable_attribute = "��������"
                 elif selected_attribute == "4":
                     alterable_attribute = "��������"
                else:
                     print("������ ����", str(selected_attribute), "�� ����������")
                     input("������� Enter, ��� �����������...")
                 ���� ���������� ���������.
                if choise == "1":                
                     change = int(input("������� �� ����� �������� ����� ��������� {}: ".format(alterable_attribute)))
             
                      �������� �� ���������� ����:                   
                     while change > attribute_points or change < 0:
                         print("��� ����� ����� ����� - ", attribute_points)
                         print("�� ������ ��������� �� {}!".format(change))
                         change = int(input("������� ������ ��������"))
                      ������ �����, �������� ��������.                               
                     attribute_points = attribute_points - change
                     attributes[alterable_attribute] += change
                  ���� ���������� ���������.
                 elif choise == "2":                
                     change = int(input("������� �� ����� �������� ����� ��������� {}: ".format(alterable_attribute)))
                      �������� �� ���������� ����:
                     while change > attributes[alterable_attribute] or change < 0:
                         print("��������, ������� �� ������ ���������, ����� {} ����/-�� ".format(alterable_attribute) )
                         print("�� ������ ��������� �� {}!".format(change))
                        change = int(input("������� ������ ��������"))
                      ������ �����, ��������� ��������.
                     attribute_points = attribute_points + change
                     attributes[alterable_attribute] -= change
             else:
                 print("������ ����", str(selected_attribute), "�� ����������")
                 input("������� Enter, ��� �����������...") 
             
     else:
        print("������ ����", str(choise), "�� ����������")
         input("������� Enter, ��� �����������...")   