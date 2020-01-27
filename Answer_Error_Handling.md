How I would implement a tool to report frontend errors of a system

Knowing how and why an error occurs is vital for a project. There are many tools available in the market. I will first review tools developers use today. Then I will explain how difficult it is to update a project to make sure the tool will be used at its full potential. Finally, I will explain how a docker can help to extract data from the chosen tool.

I/ The tools available
During the research, I found something clear : there are a lot of tools available that help debug a project. Rollbar, Crashlytics, Bugsnag, etc. all propose to debug a project. But for the sake of this challenge, I will stick with Sentry. Indeed, this platform supports both React and Ruby on Rails, which I know is used in Pyx4.
Sentry makes sure developers can monitor errors with as many information as possible. For example, for a certain error, you may be interested in knowing on which type of device the error occurred, as well as the other errors this device encountered before. Sentry makes sure these elements can be found quickly.

II/ Update of project
The update of the project based on React seems to be fast and pretty easy. Only a few lines of code are needed to install the platform (see https://sentry.io/for/react). 
The rest of the integration is to try and catch errors. Then the errors are grouped and ordered in a dashboard :
![Dashboard](images/dashboard.jpg)
This dashboard will make sure the developers can handle the errors with as many information as possible.

III/ Docker use
Lastly, I will talk about the possibility of using Docker to implement Sentry in a server. Indeed, Docker is used to create a container, a sort of virtual machine, that runs an application without the need of an OS. This solution makes sure the installation is easy and light since the application comes in a package and it requires less time to initiate.

This is how I would allow developers to handle errors in the front-end of a system. I personally have only used Symphony. Some error detection tools were available, but they were clearly not as precise as what Sentry offers.
