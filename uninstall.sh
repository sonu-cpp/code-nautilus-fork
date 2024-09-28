# Remove the vscode_extension.py file
echo "Removing Nautilus extension..."
rm -f ~/.local/share/nautilus-python/extensions/vscode_extension.py

# Restart nautilus
echo "Restarting nautilus..."
nautilus -q

echo "Uninstallation Complete"