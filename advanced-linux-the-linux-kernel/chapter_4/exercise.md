Linux Kernel Fundamentals: Chapter 4, Examining Linux Kernel Source Code

1. Fetch the kernel source as an RPM.

-> TBD

2. Fetch the Ubuntu kernel source.

-> Installed Ubuntu kernel source

3. For your kernel, do make cscope and make tags.

  -> make cscope

  -> make tags
  
4. Look at the first few lines of Makefile. What kernel version is it? Does it match uname -r? In the 
kernel Makefile, set EXTRAVERSION to -<YOUR NAME>. For example: EXTRAVERSION = -kevin.

-> EXTRAVERSION = -prashant

5. Test the ctags facility of the vi text editor.
  
  • Look up the function in the Linux kernel called sys_open(). If you find macro definitions at first, do :tn to find the next definition, and until you find the function definition.

  • The sys_open() function makes use of other functions. Move your cursor to one of these functions and hit Ctrl-]. What happened?

• Hit the key sequence Ctrl-T. What happened?

• Use the :tag command to look up the tag atomic_inc. Use the :tn command. What did this do? What does the :ts command do?

• Without changing directories, load the file 3c59x.c.

• Use the command :tags. What does this show?
