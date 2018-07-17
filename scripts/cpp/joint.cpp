/*****************************************************
BID#3                                BID#1
            setvalue drive   direct               setvalue   drive   direct
Left Hip    AO0      DO0     DO2     Right Hip    AO0        DO0     DO2
Left Knee   AO1      DO1     DO3     Right Knee   AO1        DO1     DO3
Just set the DO port to 0 is ok.
port    numDO  input    port    numDO  input
29      DO0    0x01     30      DO1    0x02
31      DO2    0x04     32      DO3    0x08
*****************************************************/
#include "../inc/DeviceLink.h"
#include "../inc/uniserial/ENCReader.h"
#include "../inc/pid.h"
#include <sys/time.h>    //struct itimerval, setitimer()
#include <math.h>
#include <signal.h>         /*signal SIGALRM*/
//#include <unistd.h>     /*Unix标准函数定义*/
#include <iomanip>
#include <fstream>
#include <ros/ros.h>
#include <neu_wgg/joint.h>

float qd_rh = 0.0;   double q_rh = 0.0;float qd_rk = 0.0;   double q_rk = 0.0;
float qd_lh = 0.0;   double q_lh = 0.0;float qd_lk = 0.0;   double q_lk = 0.0;
float AO_rh = 0.0;    float AO_rk = 0.0;float AO_lh = 0.0;    float AO_lk = 0.0;
double * dataAOR = new double [2];
double * dataAOL = new double [2];
uint8 dataDOrh = 0x00;   uint8 dataDOrk = 0x00;
uint8 dataDOlh = 0x00;   uint8 dataDOlk = 0x00;
float cTime = 0.0;

/***************************PIDControl()********************************/
int num=0;
ofstream dataOut("com.txt",ios::trunc);
void PIDControl(int num)  {

    InstantAO ao_r(deviceDescription1);
    InstantAO ao_l(deviceDescription2);
    StaticDO do_r(deviceDescription1);
    StaticDO do_l(deviceDescription2);
    Pid_control   m_Pid_rh; Pid_control   m_Pid_rk;
    Pid_control   m_Pid_lh; Pid_control   m_Pid_lk;
    //qd input
    /*
    qd_rh = 10.0*(sin(0.1*3.14159*cTime));
    qd_rk = 30.0*(1.0-cos(0.1*3.14159*cTime));
    qd_lh = 10.0*(0-sin(0.1*3.14159*cTime));
    qd_lk = 30.0*(1.0+cos(0.1*3.14159*cTime));
    cTime = cTime + 0.02;   //T = 5s
	if(cTime>2000.0)     cTime = 0.0;
	*/
    if(((qd_rh - q_rh) > -0.1)&((qd_rh - q_rh) < 0.1)) {
        dataAOR[0] = 0.0;                   dataDOrh = 0x00;
    }
    else {
        AO_rh = m_Pid_rh.PID_realize(qd_rh,q_rh, 1.0, 0.0, 0.15);
        if (AO_rh >= 0.0) {
           dataAOR[0] = AO_rh;              dataDOrh = 0x05;
        }
        else {
            dataAOR[0] = 0.0 - AO_rh;       dataDOrh = 0x01;
        }
    }

    if(((qd_rk - q_rk) > -0.1)&((qd_rk - q_rk) < 0.1)) {
        dataAOR[1] = 0.0;                   dataDOrk = 0x00;
    }
    else {
        AO_rk = m_Pid_rk.PID_realize(qd_rk,q_rk, 0.3, 0.0, 0.25);
        if (AO_rk >= 0.0) {
            dataAOR[1] = AO_rk;             dataDOrk = 0x0A;
        }
        else {
            dataAOR[1] = 0.0 - AO_rk;       dataDOrk = 0x02;
        }
    }

    if(((qd_lh - q_lh) > -0.1)&((qd_lh - q_lh) < 0.1)) {
        dataAOL[0] = 0.0;                   dataDOlh = 0x00;
    }
    else {
        AO_lh = m_Pid_lh.PID_realize(qd_lh,q_lh, 0.8, 0.0, 0.15);
        if (AO_lh >= 0.0) {
           dataAOL[0] = AO_lh;              dataDOlh = 0x01;
        }
        else {
            dataAOL[0] = 0.0 - AO_lh;       dataDOlh = 0x05;
        }
    }
    if(((qd_lk - q_lk) > -0.1)&((qd_lk - q_lk) < 0.1)) {
        dataAOL[1] = 0.0;                   dataDOlk = 0x00;
    }
    else {
        AO_lk = m_Pid_lk.PID_realize(qd_lk,q_lk, 0.15, 0.0, 0.25);
        if (AO_lk >= 0.0) {
            dataAOL[1] = AO_lk;             dataDOlk = 0x02;
        }
        else {
            dataAOL[1] = 0.0 - AO_lk;       dataDOlk = 0x0A;
        }
    }
    for(int32 j = 0; j < 2; j++)    {
        ao_r.output(j,dataAOR[j]);
        ao_l.output(j,dataAOL[j]);
        do_r.output(dataDOrh+dataDOrk);
        do_l.output(dataDOlh+dataDOlk);
    }
    if(num<10000)   {
        dataOut<<qd_rh<<"\t"<<q_rh<<"\t"<<qd_rk<<"\t"<<q_rk<<"\t"<<qd_lh<<"\t"<<q_lh<<"\t"<<qd_lk<<"\t"<<q_lk<<endl;
        num++;
    }
    else{
        dataOut.close();
        num = 0;
        dataOut.open("com.txt",ios::out);
    }
    cout.setf(ios::fixed);
    cout <<"Desired Angle: "<<setprecision(3)<<qd_rh<<"\t***\t"<<setprecision(3)<<qd_rk<<"\t***\t"<<setprecision(3)<<qd_lh<<"\t***\t"<<setprecision(3)<<qd_lk<<endl;
    cout <<"Actual  Angle: "<<setprecision(3)<<q_rh<<"\t***\t"<<setprecision(3)<<q_rk<<"\t***\t"<<setprecision(3)<<q_lh<<"\t***\t"<<setprecision(3)<<q_lk<<endl;
    cout <<"******************************************************************************"<<endl;
    delete [] dataAOR;
    delete [] dataAOL;
    ao_r.close();
    ao_l.close();

}


int main()  {

    //define a ros joint publisher
    ros::init(argc, argv, "joint_publisher");
    ros::NodeHandle n;
    ros::Publisher joint_pub = n.advertise<neu_wgg::joint>("angle_topic", 50);
    ros::Rate loop_rate(10);


//ofstream dataSave;

    int zeros[2]={0};
    int qil = 0;    int qir = 0;
    double q_lh0 = 0; double q_lk0 = 0.0; double q_rh0 = 0.0;double q_rk0 = 0.0;
    struct itimerval tick;
    signal(SIGALRM, PIDControl);
    memset(&tick, 0, sizeof(tick));
    tick.it_value.tv_sec = 2;    //Timeout to run first time
    tick.it_value.tv_usec = 0;
    tick.it_interval.tv_sec = 0;    //After first, the Interval time for clock
    tick.it_interval.tv_usec = 5000;
    if(setitimer(ITIMER_REAL,&tick, NULL)<0)
        printf("Set timer failed!\n");
    ENCReader m_ENCreader("/dev/HALLL");      //right leg Hall Angle
    ENCReader m_ENCreader1("/dev/HALLR");     //left leg Hall Angle
    ENCReader MPUReaderL("/dev/MPUL");       //left leg MPU data
    ENCReader MPUReaderR("/dev/MPUR");       //right leg MPU data

    if(!(m_ENCreader.OpenReader()&m_ENCreader1.OpenReader()&MPUReaderL.OpenReader()&MPUReaderR.OpenReader()))
        cout << "Open Com Port Failed!" << endl;
    else {
        m_ENCreader.PresetValues(zeros);
        m_ENCreader1.PresetValues(zeros);
        MPUReaderL.m_serial.Flush();
        MPUReaderR.m_serial.Flush();
        sleep(1);
        int m = 0;
        float qd_lh0 = 0.0;float qd_lh_old = 0.0;     float qd_lk0 = 0.0;float qd_lk_old = 0.0;
        float qd_rh0 = 0.0;float qd_rh_old = 0.0;     float qd_rk0 = 0.0;float qd_rk_old = 0.0;

//    dataSave.open("com.txt",ios::ate);
        while(ros::ok()) {
            neu_wgg::joint joint_msg;
//        for(int ti = 0; ti<10000;ti++)  {
//            dataSave<<"888"<<"\n";
            if((MPUReaderL.UpdateValuesMPU())&(MPUReaderR.UpdateValuesMPU())) {
                float m_qd_lh_in = (float)MPUReaderL.MPUs[0];float m_qd_lk_in = (float)MPUReaderL.MPUs[1];
                float m_qd_rh_in = (float)MPUReaderR.MPUs[0];float m_qd_rk_in = (float)MPUReaderR.MPUs[1];
                if(m<100)    {
                    qd_lh = 0.0;qd_lk = 0.0;qd_rh = 0.0; qd_rk = 0.0;
                    qd_lh0 = m_qd_lh_in + qd_lh0;   qd_lk0 = m_qd_lk_in + qd_lk0;  qd_rh0 = m_qd_rh_in + qd_rh0;    qd_rk0 = m_qd_rk_in + qd_rk0;
                    m++;
                }
                else if(m==100)  {
                    qd_lh0 = qd_lh0 / 100;  qd_lk0 = qd_lk0 / 100;   qd_rh0 = qd_rh0 / 100;  qd_rk0 = qd_rk0 / 100;
                    m++;
                }
                else{
                    float m_qd_lh = qd_lh0 - m_qd_lh_in;
                    float m_qd_lk = qd_lk0 - m_qd_lk_in;
                    float m_qd_rh = qd_rh0 - m_qd_rh_in;
                    float m_qd_rk = m_qd_rk_in - qd_rk0;
                    if(abs(m_qd_lh - qd_lh_old)<20)    {
                        qd_lh = m_qd_lh;   qd_lh_old = m_qd_lh;
                    }
                    else
                        qd_lh = qd_lh_old;
                    if(abs(m_qd_lk - qd_lk_old)<20)    {
                        qd_lk = m_qd_lk;   qd_lk_old = m_qd_lk;
                    }
                    else
                        qd_lk = qd_lk_old;
                    qd_lk = qd_lk - qd_lh;
                    if(abs(m_qd_rh - qd_rh_old)<20)    {
                        qd_rh = m_qd_rh;   qd_rh_old = m_qd_rh;
                    }
                    else
                        qd_rh = qd_rh_old;
                    if(abs(m_qd_rk - qd_rk_old)<20)    {
                        qd_rk = m_qd_rk;   qd_rk_old = m_qd_rk;
                    }
                    else
                        qd_rk = qd_rk_old;
                    qd_rk = qd_rk - qd_rh;
//                    cout<<qd_lh<<"***"<<qd_lk<<"***"<<qd_rh<<"***"<<m_qd_rk_in<<endl;
                }

            }
            else
                cout<<"update mpu error"<<endl;

            double conversionHall = 360.0/120.0/(6.0*12.0);
            if(m_ENCreader.UpdateValues()) {
                double m_q_rh = (double)m_ENCreader.ENCs[0] * conversionHall;
                double m_q_rk = (double)m_ENCreader.ENCs[1] * conversionHall;
                if (qil == 0)    {
                    q_rh0 = m_q_rh;           q_rk0 = m_q_rk;
                    qil++;
                }
                else    {
                    q_rh = m_q_rh - q_rh0;    q_rk = m_q_rk - q_rk0;
                }
            }
            else
                cout<<"UpdateValues error"<<endl;
            m_ENCreader.m_serial.Flush();
            if(m_ENCreader1.UpdateValues()) {
                double m_q_lh = (double)m_ENCreader1.ENCs[0] * conversionHall;
                double m_q_lk = (double)m_ENCreader1.ENCs[1] * conversionHall;
                if (qir == 0)    {
                    q_lh0 = m_q_lh;            q_lk0 = m_q_lk;
                    qir++;
                }
                else    {
                    q_lh = q_lh0 - m_q_lh;     q_lk = q_lk0 - m_q_lk;
                }
            }
            else
                cout<<"UpdateValues error"<<endl;
            joint_msg.eleftk = qd_lk;
            joint_msg.elefth = qd_lh;
            joint_msg.erightk = qd_rk;
            joint_msg.erighth = qd_rh;
            joint_msg.leftk = q_lk;
            joint_msg.lefth = q_lh;
            joint_msg.rightk = q_rk;
            joint_msg.righth = q_rh;
            joint_pub.publish(joint_msg);
            ros::spinOnce();
            loop_rate.sleep();
            m_ENCreader1.m_serial.Flush();

        }
//        dataSave.close();
    }
    cout<<"Ending..."<<endl;
}
