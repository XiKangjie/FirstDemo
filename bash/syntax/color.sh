#!/usr/bin/env bash
set -e

# escape sequences: <Esc>[FormatCodem
# in bash, the <Esc> character can be obtained with the following syntaxes:
# \e    \033    \x1B
# <Esc>[0m sequence removes all attributes (formatting and colors)

# Bash uses numeric codes to set attributes of the text to be displayed,
# any missing code is simply taken as zero value by bash.
# \e[attribute code;text color code;background color codem

# Attribute codes:
# 00=none 01=bold 04=underscore 05=blink 07=reverse 08=concealed 

# Text color codes:
# 30=black 31=red 32=green 33=yellow 34=blue 35=magenta 36=cyan 37=white

# Background color codes:
# 40=black 41=red 42=green 43=yellow 44=blue 45=magenta 46=cyan 47=white

color_red="\e[0;31m"
color_green="\e[0;32m"
color_yellow="\e[0;33m"
color_blue="\e[0;34m"
color_end="\e[0m"

echo -e "  [ ${color_red}red${color_end} ]"
echo -e "  [ ${color_green}green${color_end} ]"
echo -e "  [ ${color_yellow}yellow${color_end} ]"
echo -e "  [ ${color_blue}blue${color_end} ]"

echo

echo_ok()
{
    echo -e "  [ ${color_green}OK${color_end} ] $1"
}

echo_error()
{
    echo -e "  [ ${color_red}ERROR${color_end} ] $1"
}

echo_warn()
{
    echo -e "  [ ${color_yellow}?${color_end} ] $1"
}

echo_info()
{
    echo -e "  [ ${color_blue}...${color_end} ] $1"
}

echo_ok "All Done!"
echo_error "There is no Vim"
echo_warn "[Y/N]"
echo_info "Installing Vim"
