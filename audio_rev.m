inputfile='/home/smouneswar/Documents/week-8/sample-3s.wav'
outputfile='/home/smouneswar/Documents/week-8/sample-3s.wav'
[y,Fs]=audioread(inputfile);
reversedData=flipud(y);
audiowrite(outputfile,reversedData,Fs);
disp('audio is reversed and successfully saved')
