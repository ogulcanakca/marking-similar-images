# Marking Similar Images

It is an application to generate similarity marking data that can be given as input to a machine learning model in Python using the Flask library.

## Installation

* By running these .py files in the following order, the system will run without Containerization.
1.	trendyol_urun_bilgisi.py
2.	Exceldownloader.py
3.	imagedownloader.py
4.	app.py

* In the following order, the system will both be turned into a Container locally and run smoothly, and deployed to Azure Cloud and a site that everyone can access will be created smoothly.

1.	Download and install Azure Cli.
2.	In cmd, use cd to go to the directory where the application is located. For example "cd C:\Users\ogulc\Desktop\task". The application is in the desktop\task directory.
3.	After Docker desktop is opened, type "Docker image build -t <imageadi> ." including the dot in cmd and run it. Do not close cmd. This will build the Docker image.
- If Container is wanted to run in Local;
4.	Container can be created using an image. After typing "Docker Container run -p 5000:5000 <imageadi>" in cmd, the Container is created and the system runs.
- If  Web Application is wanted to make by deploying to Azure Cloud;
5.	If there is no Azure, it should be created and if there is, the account should be entered. Then search for "Resource Groups" from Azure Portal.
6.	If a Resource Group does not need to be created (if it already exists) go to point 8. If a new Resource Group needs to be created, click on Create. 
7.	After typing the Resource Group name, click Review + Create. Then click Create.
8.	Return to Azure Portal. Then enter the Resource Group and press the Create button.
9.	After searching for "Container Registry" on the redirected page, click on the first one and press the Create button on the redirected page. 
10.	After typing the Registry name on the redirected page, press Review+Create and then creat. Also, after entering the Container Registry, the admin user option must be enabled in the Access keys tab.
Thus the Container Registry is created. In the Container Registry, the application that has been made into a Docker image is deployed. This Registry acts as a kind of repository, similar to a Github repository or DockerHub.
11.	After typing "az acr build --file Dockerfile --Registry <ContainerRegistryAdi> –image <imageadi> .” in cmd and click enter. az command comes with Azure Cli downloaded and installed in point 1. So step 1 must be done. <imageadi> is the image created in step 3. <ContainerRegistryAdi> is the Container Registry created in point 10. Dockerfile is the Docker file in the directory where we are in cmd (in this case the task folder). After waiting for about 5 minutes for the image to be deployed to the Registry, the Registry created in step 10 needs to be entered from the Azure Portal. If these have been created, continue with the next step. 
12.	After re-entering the Resource Group created in step 6, search for "Web App" from the search tab. Then it should be created with the Create button. 
13.	On the page that opens, fill in the name in the Instance Details section. Pricing plan B1 is quite sufficient for this application. More should be changed if necessary. Publish option should be Docker Container and Operating System should be Linux. Then click Next: Docker and select Azure Container Registry as the Image Source option on the page that opens. In the Azure Container Registry options tab, the Registry option should automatically select the Registry created in item 10. If not, it should be selected manually. In the Image option, the image deployed to the Registry created in item 10 in item 11 should be selected. Then "Review + Create" button should be pressed.
14.	After re-entering the Resource Group created in step 6, press the Create button, search for SQL database and create the second option by pressing the Create button.
15.	On the redirected screen, put the database name and then press the "Create new" button to create a Server. 
16.	After naming the server, select authentication method "Use both SQL and Azure AD authentication". In Azure admin section, click on set admin and in search section, find and select the account in Azure Portal. Server admin login and password should be filled according to user request. After pressing the Ok button, you need to return to the previous screen (step 15).
17.	After selecting Workload environment option Development, select Backup storage redundancy option "Geo-redundant backup storage" and click Next:Networking. 
18.	On the redirected screen, connectivity method option "Public endpoint" should be selected, firewall rules and connection policy should be left selected as default. After pressing "Rewiev + Create" button, "Create" button should be pressed.
19.	From the SQL Server Management Studio application, log in to the server with the server admin and password created in step 16.
20.	Create a table with username and password and another table with positive_images, negative_images, image_name and username columns for similarity marking.
After these steps, the system should run smoothly. 


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
