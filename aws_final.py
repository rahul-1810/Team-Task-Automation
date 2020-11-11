import os
import getpass
os.system('clear')
os.system('tput setaf 1')
os.system('figlet A W S Automation')
os.system("tput setaf 3")
print("\t\t\t -----------------------------")
os.system("tput setaf 3")
print("\t\t\t Welcome to AWS Automation..!!")
os.system("tput setaf 6")
print("\t          A           W                   W       S S S S S S S S	")
print("\t         A A           W                 W        S	              	")  
print("\t        A   A           W               W         S  			")
print("\t       A A A A           W             W          S S S S S S S S   	")           
print("\t      A       A           W     W     W                         S	")
print("\t     A         A           W  W   W  W                          S	")               
print("\t    A           A           W       W             S S S S S S S S   	")
os.system("tput setaf 3")                                                       
print("\t\t\t -----------------------------")

os.system('tput setaf  5')
print(""" Press 1 :  To Login in AWS
 press 2 :  Describe All Instances
 press 3 :  To Create New Key-Pair
 press 4 :  To Create New Security Group
 Press 5 :  To Create a Volume
 Press 6 :  Extract subnet id
 Press 7 :  Launch a Instance (aws linux)
 Press 8 :  Start instance
 Press 9 :  Stop instance
 Press 10 : Attach volume with instance
 Press 11 : Create a S3 Bucket
 Press 12 : Upload a local file(or image) to the S3 bucket
 Press 13 : Create CloudFront Distribution using origin as S3 Object-url
 Press 14 : Exit
 """)	
os.system('tput setaf 3')
while True:
	ch = input("Enter your Choice :-  ")
	print(ch)
	if int(ch) == 1:
		os.system("aws configure")
		os.system("python3 aws_final.py")

	if int(ch) == 2:
		os.system("aws ec2 describe-instances \
    --filters Name=tag-key,Values=Name \
    --query 'Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==`Name`]|[0].Value}' \
    --output table")
		os.system("python3 aws_final.py")

	if int(ch) == 3:
		key_name = input("Enter Key-Pair Name :")
		os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
		os.system("python3 aws_final.py")

	if int(ch) == 4:
		sg_grp = input("Enter Security Group Name :")
		des = input("Enter Security Group Description :")
		os.system("aws ec2 create-security-group --group-name {} --description {}".format(sg_grp,des))
		os.system("python3 aws_final.py")

	if int(ch) == 5:
		vol = input("Enter Volume Size :-")
		az = input("Enter Availability Zone :-")
		os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {}".format(vol,az))
		os.system("python3 aws_final.py")

	if int(ch) == 6:
		os.system("aws ec2 describe-subnets --query Subnets[0].[SubnetId]")
		os.system("python3 aws_final.py")
        
	if int(ch) == 7:
		print("""
		Press 1:AWS Linux
		Press 2:Redhat Linux
		""")

		print("Enter your Choice :  ",end="")
		img=input()
		if int(img) ==1:
			key = input("Enter your key:-")
			sg_grp = input("Enter your security grp:-")
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(key,sg_grp))
			print("Successfully launched instance!")
			os.system("python3 aws_final.py")

		if int(img) == 2:
			key = input("Enter your key:-")
			sg_grp = input("Enter your security grp:-")
			os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(key,sg_grp))
			print("Successfully launched instance!")
			os.system("python3 aws_final.py")


	if int(ch) == 8:
		sti = input("Enter Instance Id:- ")
		os.system(" aws ec2 start-instances --instance-id {}".format(sti))
		os.system("python3 aws_final.py")


	if int(ch) == 9:
		spi = input("Enter Instance Id :- ")
		os.system(" aws ec2 stop-instances --instance-id {}".format(spi))
		os.system("python3 aws_final.py")


	if int(ch) == 10: 	
		vol_id = input("Enter Volume ID :- ")	
		ins_id = input("Enter Instance ID:- ")
		os.system(" aws ec2 attach-volume  --volume-id {} --instance-id {} --device /dev/sdf".format(vol_id,ins_id))
		os.system("python3 aws_final.py")


	if int(ch) == 11:
		bk_name=input("Enter Bucket Name")
		rgn = input("Enter region Name")
		os.system("aws s3 mb s3://{} --region {}".format(bk_name,rgn))
		os.system("python3 aws_final.py")


	if int(ch) == 12:  
		bname= input("Enter your bucket name: ")
		path = input("Enter Object path :-")
		os.system("aws s3 cp {} s3://{} --acl public-read".format(path,bname))
		os.system("python3 aws_final.py")




	if int(ch) == 13:
		print("Enter your s3 bucket name: ",end= "")
		bname = input()
		print("Enter region where s3 create a bucket (such as ap-south-1): ",end = "")
		region_name = input()
		os.system(" aws cloudfront create-distribution --origin-domain-name {}.s3.{}.amazonaws.com ".format(bname,region_name))
		os.system("python3 aws_final.py")


	if int(ch) == 14:
		print("\t\t\t -----------------------------")
		os.system("tput setaf 3")
		print("\t\t\t You are exited from the Menu")
		os.system("tput setaf 7")
		print("\t\t\t -----------------------------")
		exit()

	else:
		
		print("\t\t\t -----------------------------")
		os.system("tput setaf 3")
		print("\t\t\t\t Invalid Option..!!")
		print("\t\t\t You are exited from the Menu")
		os.system("tput setaf 7")
		print("\t\t\t -----------------------------")
		exit()
