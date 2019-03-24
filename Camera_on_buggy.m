

flag = 0;

while (flag == 0)
    
    prompt= 'What is distance?      ';
    distance = input (prompt);
    for i = 1:1000
     
        while (distance > 0 && flag==0)
            
            if (distance<=200 && distance >115)
                choice = 1;
            elseif (distance<=115 && distance >65)
                choice = 2;
            elseif (distance<=65 && distance >45)
                choice = 3;
            elseif (distance<=45 && distance >0)
                choice = 4;
            end
           

            switch choice
                case 1
                    low = 15;
                    high = 25;
                    T = 240;
                    S = 0.93;
                    [centers, radius] = Acquire_center(low, high, T, S);
                    
                case 2
                    low = 20;
                    high = 40;
                    T = 230;
                    S = 0.95;
                    [centers, radius] = Acquire_center(low, high, T, S);
                    
                                   
                case 3
                    low = 15;
                    high = 20;
                    T = 150;
                    S = 0.96;
                    [centers, radius] = Acquire_center(low, high, T, S);
                    
                case 4
                    low = 50;
                    high = 150;
                    T = 250;
                    S = 0.96;
                    [centers, radius] = Acquire_center(low, high, T, S);
                    
            end
            
           switch i
                case 1
                    center_x_1 = centers(1:1);
                    center_x_n = centers(1:1);
                    disp(center_x_n);
                otherwise
                    center_x_n = centers(1:1);
           end
            disp('deviation = ');
            deviation = abs(center_x_n - center_x_1);
            disp(deviation);
            if deviation > 20
                disp('Error!   ');
            
            end
            i=i+1;
            %disp(i);
            
            distance = distance - 5;
            %disp('new distance');
            %disp(distance);
            stop = 'Continue?   Input 1 to stop, and 0 to continue    ';   % An input from motor which tells me whether continue taking the image or not
            flag = input (stop);
            %disp(flag);
        end
    
    end
    
    stop = 'Restart?  Input 1 to stop, and 0 to restart    ';   % An input from motor which tells me whether the motor is turing and a new distance input is needed
    flag = input (stop);
end



